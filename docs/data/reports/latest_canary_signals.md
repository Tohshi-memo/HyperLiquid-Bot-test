# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T21:37:32.981562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0454` n `12`; crypto_alt avg `-0.0357` n `233`; crypto_major avg `-0.046` n `8`; equity avg `-0.0824` n `136`; fx avg `0.009` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0055` n `20`; unknown avg `12.7682` n `796`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.1201` n `233`; crypto_major avg `-0.1559` n `8`; equity avg `-0.1002` n `136`; fx avg `-0.0073` n `6`; index avg `-0.0013` n `26`; metal avg `0.0376` n `20`; unknown avg `9.7395` n `776`
- 4h: commodity avg `0.3161` n `12`; crypto_alt avg `-0.2956` n `233`; crypto_major avg `-0.2237` n `8`; equity avg `-0.5736` n `136`; fx avg `0.0122` n `6`; index avg `-0.0261` n `26`; metal avg `-0.1911` n `20`; unknown avg `4.2886` n `750`
- 24h: commodity avg `1.1997` n `12`; crypto_alt avg `-2.6885` n `233`; crypto_major avg `-2.2273` n `8`; equity avg `-2.098` n `136`; fx avg `0.1098` n `6`; index avg `-0.3207` n `26`; metal avg `-1.2383` n `20`; unknown avg `-1.3226` n `667`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal

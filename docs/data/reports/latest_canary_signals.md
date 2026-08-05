# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T10:52:28.749826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0452` n `12`; crypto_alt avg `-0.1437` n `230`; crypto_major avg `-0.1852` n `8`; equity avg `-0.197` n `108`; fx avg `-0.0094` n `6`; index avg `-0.0198` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.0154` n `782`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.1814` n `230`; crypto_major avg `-0.2908` n `8`; equity avg `-0.1951` n `108`; fx avg `-0.0049` n `6`; index avg `-0.02` n `25`; metal avg `-0.0635` n `20`; unknown avg `0.0038` n `781`
- 4h: commodity avg `0.3187` n `12`; crypto_alt avg `-0.3049` n `230`; crypto_major avg `-0.3139` n `8`; equity avg `-0.8893` n `108`; fx avg `0.0191` n `6`; index avg `-0.1239` n `25`; metal avg `-0.275` n `20`; unknown avg `0.6613` n `781`
- 24h: commodity avg `-0.9397` n `12`; crypto_alt avg `0.374` n `230`; crypto_major avg `0.324` n `8`; equity avg `2.0244` n `108`; fx avg `-0.0126` n `6`; index avg `0.5679` n `25`; metal avg `0.9306` n `20`; unknown avg `0.1072` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal

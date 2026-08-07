# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:54:56.739268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0448` n `230`; crypto_major avg `-0.0034` n `8`; equity avg `0.0362` n `112`; fx avg `-0.0006` n `6`; index avg `0.0034` n `25`; metal avg `0.0304` n `20`; unknown avg `0.0008` n `782`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `-0.2415` n `230`; crypto_major avg `-0.0835` n `8`; equity avg `0.1628` n `112`; fx avg `0.013` n `6`; index avg `0.0071` n `25`; metal avg `-0.0478` n `20`; unknown avg `0.0202` n `782`
- 4h: commodity avg `-0.255` n `12`; crypto_alt avg `-0.2832` n `230`; crypto_major avg `-0.1227` n `8`; equity avg `0.318` n `112`; fx avg `-0.0029` n `6`; index avg `0.0519` n `25`; metal avg `0.0656` n `20`; unknown avg `-0.1186` n `782`
- 24h: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.1937` n `230`; crypto_major avg `-0.0157` n `8`; equity avg `2.131` n `112`; fx avg `-0.1506` n `6`; index avg `0.12` n `25`; metal avg `0.3507` n `20`; unknown avg `-0.0105` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal

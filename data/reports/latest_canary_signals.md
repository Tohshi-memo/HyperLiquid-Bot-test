# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T16:54:07.959291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.1372` n `230`; crypto_major avg `0.0131` n `8`; equity avg `0.0281` n `102`; fx avg `0.0234` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0494` n `20`; unknown avg `-0.0482` n `780`
- 1h: commodity avg `0.1655` n `12`; crypto_alt avg `0.2778` n `230`; crypto_major avg `0.0879` n `8`; equity avg `0.4993` n `102`; fx avg `0.0403` n `6`; index avg `0.0761` n `25`; metal avg `-0.0743` n `20`; unknown avg `-0.2072` n `780`
- 4h: commodity avg `-0.1864` n `12`; crypto_alt avg `0.1152` n `230`; crypto_major avg `-0.8939` n `8`; equity avg `-1.6846` n `102`; fx avg `-0.0577` n `6`; index avg `-0.1597` n `25`; metal avg `-0.086` n `20`; unknown avg `0.1717` n `780`
- 24h: commodity avg `0.0509` n `12`; crypto_alt avg `-0.3638` n `230`; crypto_major avg `-1.8574` n `8`; equity avg `0.5385` n `102`; fx avg `0.1316` n `6`; index avg `0.3189` n `25`; metal avg `-0.3774` n `20`; unknown avg `0.567` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal

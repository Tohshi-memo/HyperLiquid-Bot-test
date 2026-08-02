# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T13:22:24.853589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `0.051` n `8`; equity avg `0.0197` n `102`; fx avg `0.0064` n `6`; index avg `0.009` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0012` n `782`
- 1h: commodity avg `0.0883` n `12`; crypto_alt avg `-0.1497` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `0.0294` n `102`; fx avg `-0.0025` n `6`; index avg `0.0131` n `25`; metal avg `0.0237` n `20`; unknown avg `-0.042` n `782`
- 4h: commodity avg `0.3205` n `12`; crypto_alt avg `-0.2953` n `230`; crypto_major avg `-0.341` n `8`; equity avg `-0.1078` n `102`; fx avg `-0.0073` n `6`; index avg `-0.0343` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.1275` n `782`
- 24h: commodity avg `-1.0353` n `12`; crypto_alt avg `0.1351` n `230`; crypto_major avg `0.0249` n `8`; equity avg `0.8516` n `102`; fx avg `-0.0986` n `6`; index avg `0.2204` n `25`; metal avg `0.2455` n `20`; unknown avg `0.2175` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal

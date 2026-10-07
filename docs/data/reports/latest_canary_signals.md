# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T06:07:31.419992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0716` n `13`; crypto_alt avg `-0.1621` n `235`; crypto_major avg `-0.0455` n `8`; equity avg `-0.1036` n `150`; fx avg `-0.0047` n `6`; index avg `-0.0265` n `26`; metal avg `-0.0522` n `20`; unknown avg `0.0521` n `1052`
- 1h: commodity avg `0.0609` n `13`; crypto_alt avg `0.2205` n `235`; crypto_major avg `0.2506` n `8`; equity avg `-0.049` n `150`; fx avg `-0.0058` n `6`; index avg `-0.0253` n `26`; metal avg `-0.0551` n `20`; unknown avg `0.6845` n `1052`
- 4h: commodity avg `0.1362` n `13`; crypto_alt avg `0.2699` n `235`; crypto_major avg `0.6851` n `8`; equity avg `0.1884` n `150`; fx avg `-0.0302` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0858` n `20`; unknown avg `1.6028` n `1046`
- 24h: commodity avg `0.6048` n `13`; crypto_alt avg `-2.721` n `235`; crypto_major avg `-1.6575` n `8`; equity avg `-0.1394` n `149`; fx avg `0.0652` n `6`; index avg `-0.0693` n `26`; metal avg `-0.0105` n `20`; unknown avg `871.1578` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal

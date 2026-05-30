# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T03:07:17.849322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.0161` n `228`; crypto_major avg `0.0982` n `8`; equity avg `0.0105` n `69`; fx avg `-0.0027` n `6`; index avg `-0.0009` n `23`; metal avg `-0.044` n `18`; unknown avg `0.0554` n `419`
- 1h: commodity avg `-0.142` n `12`; crypto_alt avg `0.1805` n `228`; crypto_major avg `0.0819` n `8`; equity avg `0.0478` n `69`; fx avg `0.0005` n `6`; index avg `-0.0164` n `23`; metal avg `0.0096` n `18`; unknown avg `-0.3108` n `419`
- 4h: commodity avg `-0.0489` n `12`; crypto_alt avg `1.6745` n `228`; crypto_major avg `1.252` n `8`; equity avg `0.3341` n `69`; fx avg `-0.0103` n `6`; index avg `-0.0049` n `23`; metal avg `0.0384` n `18`; unknown avg `-0.2262` n `419`
- 24h: commodity avg `-0.1028` n `12`; crypto_alt avg `2.4506` n `228`; crypto_major avg `2.3569` n `8`; equity avg `1.2597` n `69`; fx avg `0.1049` n `6`; index avg `0.1611` n `23`; metal avg `0.1094` n `18`; unknown avg `0.6592` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal

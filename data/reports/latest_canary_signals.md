# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T00:58:53.261592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0558` n `13`; crypto_alt avg `-0.3844` n `236`; crypto_major avg `-0.2097` n `8`; equity avg `-0.3751` n `151`; fx avg `0.0313` n `6`; index avg `-0.0653` n `26`; metal avg `0.0081` n `20`; unknown avg `1.8118` n `1136`
- 1h: commodity avg `-0.1165` n `13`; crypto_alt avg `-0.4182` n `236`; crypto_major avg `-0.0681` n `8`; equity avg `0.0199` n `151`; fx avg `0.112` n `6`; index avg `-0.1032` n `26`; metal avg `0.1692` n `20`; unknown avg `0.6459` n `1128`
- 4h: commodity avg `-0.1639` n `13`; crypto_alt avg `-0.2126` n `236`; crypto_major avg `-0.0538` n `8`; equity avg `-1.4148` n `151`; fx avg `0.1668` n `6`; index avg `-0.3172` n `26`; metal avg `0.2117` n `20`; unknown avg `2.5069` n `1040`
- 24h: commodity avg `-0.4126` n `13`; crypto_alt avg `-3.0054` n `236`; crypto_major avg `-2.4506` n `8`; equity avg `-5.8828` n `151`; fx avg `0.0213` n `6`; index avg `-0.9201` n `26`; metal avg `-0.5912` n `20`; unknown avg `1393.3716` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T04:37:25.072796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `-0.1363` n `238`; crypto_major avg `-0.2238` n `8`; equity avg `-0.0499` n `156`; fx avg `-0.0005` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0014` n `20`; unknown avg `0.7158` n `1262`
- 1h: commodity avg `-0.0146` n `13`; crypto_alt avg `-0.2919` n `238`; crypto_major avg `-0.3736` n `8`; equity avg `-0.0414` n `156`; fx avg `0.0077` n `6`; index avg `-0.0172` n `27`; metal avg `-0.0051` n `20`; unknown avg `0.4883` n `1246`
- 4h: commodity avg `0.082` n `13`; crypto_alt avg `-1.0135` n `238`; crypto_major avg `-0.6836` n `8`; equity avg `-0.0652` n `156`; fx avg `0.0063` n `6`; index avg `-0.0653` n `27`; metal avg `-0.027` n `20`; unknown avg `7.7134` n `1234`
- 24h: commodity avg `-0.0032` n `13`; crypto_alt avg `1.6636` n `238`; crypto_major avg `-1.3539` n `8`; equity avg `-2.8669` n `156`; fx avg `-0.0764` n `6`; index avg `-0.2476` n `27`; metal avg `-0.6332` n `20`; unknown avg `3.1048` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal

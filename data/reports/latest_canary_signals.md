# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T06:37:25.027233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0654` n `13`; crypto_alt avg `-0.0672` n `239`; crypto_major avg `-0.0982` n `8`; equity avg `0.084` n `163`; fx avg `-0.0086` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0169` n `20`; unknown avg `0.5865` n `1264`
- 1h: commodity avg `-0.1563` n `13`; crypto_alt avg `0.152` n `239`; crypto_major avg `-0.2022` n `8`; equity avg `0.0679` n `163`; fx avg `0.0001` n `6`; index avg `0.0207` n `27`; metal avg `-0.1209` n `20`; unknown avg `-0.0094` n `1238`
- 4h: commodity avg `-0.263` n `13`; crypto_alt avg `0.3899` n `239`; crypto_major avg `0.2974` n `8`; equity avg `0.4765` n `163`; fx avg `0.0063` n `6`; index avg `0.0814` n `27`; metal avg `-0.2058` n `20`; unknown avg `2.9431` n `1226`
- 24h: commodity avg `-0.0448` n `13`; crypto_alt avg `0.7585` n `239`; crypto_major avg `1.0206` n `8`; equity avg `0.9441` n `163`; fx avg `-0.0922` n `6`; index avg `0.0581` n `27`; metal avg `-0.8902` n `20`; unknown avg `495.7353` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal

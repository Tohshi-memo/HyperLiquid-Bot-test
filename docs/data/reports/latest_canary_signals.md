# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T13:22:25.787152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.1906` n `230`; crypto_major avg `-0.2362` n `8`; equity avg `-0.0794` n `96`; fx avg `0.0056` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0207` n `770`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.145` n `230`; crypto_major avg `-0.1624` n `8`; equity avg `-0.1072` n `96`; fx avg `0.0042` n `6`; index avg `-0.008` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0003` n `770`
- 4h: commodity avg `0.0943` n `12`; crypto_alt avg `-0.0651` n `230`; crypto_major avg `-0.1281` n `8`; equity avg `-0.1472` n `96`; fx avg `-0.0025` n `6`; index avg `-0.0265` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0522` n `769`
- 24h: commodity avg `0.3816` n `12`; crypto_alt avg `-0.0148` n `230`; crypto_major avg `0.6434` n `8`; equity avg `1.376` n `96`; fx avg `0.0254` n `6`; index avg `0.2855` n `25`; metal avg `0.4372` n `20`; unknown avg `0.0438` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T15:22:38.341674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0732` n `13`; crypto_alt avg `0.4355` n `238`; crypto_major avg `0.2456` n `8`; equity avg `-0.1668` n `156`; fx avg `0.0118` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0351` n `20`; unknown avg `-0.2869` n `1259`
- 1h: commodity avg `-0.0173` n `13`; crypto_alt avg `1.5435` n `238`; crypto_major avg `1.2416` n `8`; equity avg `0.0323` n `156`; fx avg `0.018` n `6`; index avg `0.0591` n `27`; metal avg `0.1185` n `20`; unknown avg `0.5625` n `1231`
- 4h: commodity avg `0.0195` n `13`; crypto_alt avg `0.7541` n `238`; crypto_major avg `0.0599` n `8`; equity avg `-1.0414` n `156`; fx avg `-0.0942` n `6`; index avg `-0.0276` n `27`; metal avg `-0.254` n `20`; unknown avg `3.9682` n `1147`
- 24h: commodity avg `0.757` n `13`; crypto_alt avg `-4.6379` n `238`; crypto_major avg `-3.8835` n `8`; equity avg `-5.601` n `156`; fx avg `-0.1165` n `6`; index avg `-0.459` n `27`; metal avg `-0.8829` n `20`; unknown avg `38.5571` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal

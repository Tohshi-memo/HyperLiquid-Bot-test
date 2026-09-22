# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T21:52:28.711417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0401` n `234`; crypto_major avg `0.0624` n `8`; equity avg `-0.021` n `140`; fx avg `-0.0004` n `6`; index avg `0.0001` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.081` n `944`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `0.1936` n `234`; crypto_major avg `0.1946` n `8`; equity avg `0.0032` n `140`; fx avg `-0.0034` n `6`; index avg `0.0103` n `26`; metal avg `-0.0137` n `20`; unknown avg `-0.0948` n `942`
- 4h: commodity avg `0.0508` n `12`; crypto_alt avg `0.5225` n `234`; crypto_major avg `0.057` n `8`; equity avg `0.1286` n `140`; fx avg `-0.0193` n `6`; index avg `0.0112` n `26`; metal avg `0.1632` n `20`; unknown avg `0.7275` n `906`
- 24h: commodity avg `0.1796` n `12`; crypto_alt avg `2.6056` n `234`; crypto_major avg `0.4052` n `8`; equity avg `0.8635` n `140`; fx avg `-0.3083` n `6`; index avg `0.1358` n `26`; metal avg `0.2995` n `20`; unknown avg `1.5684` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T08:37:27.428486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `0.095` n `228`; crypto_major avg `0.1609` n `8`; equity avg `0.0514` n `88`; fx avg `-0.0035` n `6`; index avg `0.0096` n `23`; metal avg `0.0032` n `20`; unknown avg `-0.03` n `764`
- 1h: commodity avg `-0.0694` n `12`; crypto_alt avg `0.1074` n `228`; crypto_major avg `0.2205` n `8`; equity avg `0.1374` n `88`; fx avg `-0.0148` n `6`; index avg `0.0498` n `23`; metal avg `-0.0012` n `20`; unknown avg `5.5892` n `756`
- 4h: commodity avg `0.065` n `12`; crypto_alt avg `0.011` n `228`; crypto_major avg `0.3729` n `8`; equity avg `0.2118` n `88`; fx avg `-0.0005` n `6`; index avg `0.0366` n `23`; metal avg `-0.0312` n `20`; unknown avg `0.6548` n `724`
- 24h: commodity avg `0.2358` n `12`; crypto_alt avg `-0.0877` n `228`; crypto_major avg `-0.8497` n `8`; equity avg `0.0309` n `88`; fx avg `-0.02` n `6`; index avg `-0.0736` n `23`; metal avg `-0.0434` n `20`; unknown avg `16.8037` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal

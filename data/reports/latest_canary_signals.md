# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T07:07:20.133765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.0967` n `228`; crypto_major avg `-0.0978` n `8`; equity avg `-0.0074` n `65`; fx avg `0.0` n `5`; index avg `0.0111` n `23`; metal avg `-0.0043` n `18`; unknown avg `0.1422` n `376`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `-0.5245` n `228`; crypto_major avg `-0.291` n `8`; equity avg `0.018` n `65`; fx avg `0.0015` n `5`; index avg `0.0308` n `23`; metal avg `-0.0064` n `18`; unknown avg `-0.1983` n `376`
- 4h: commodity avg `0.0898` n `12`; crypto_alt avg `-0.3814` n `228`; crypto_major avg `-0.16` n `8`; equity avg `-0.0226` n `65`; fx avg `0.0183` n `5`; index avg `0.0653` n `23`; metal avg `-0.0994` n `18`; unknown avg `-0.1612` n `355`
- 24h: commodity avg `0.0918` n `12`; crypto_alt avg `4.6239` n `228`; crypto_major avg `2.9632` n `8`; equity avg `3.3753` n `65`; fx avg `0.0056` n `5`; index avg `1.3095` n `23`; metal avg `-0.1623` n `18`; unknown avg `1.1753` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal

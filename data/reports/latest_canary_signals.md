# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T23:07:32.997481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `-0.1685` n `235`; crypto_major avg `0.0171` n `8`; equity avg `0.0057` n `144`; fx avg `-0.0056` n `6`; index avg `0.004` n `26`; metal avg `-0.0321` n `20`; unknown avg `0.5924` n `1077`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `-0.253` n `235`; crypto_major avg `-0.1248` n `8`; equity avg `0.0236` n `144`; fx avg `0.001` n `6`; index avg `-0.0008` n `26`; metal avg `-0.033` n `20`; unknown avg `0.1282` n `1077`
- 4h: commodity avg `0.0587` n `13`; crypto_alt avg `0.7299` n `235`; crypto_major avg `0.6814` n `8`; equity avg `0.1892` n `144`; fx avg `0.0093` n `6`; index avg `0.0007` n `26`; metal avg `-0.0446` n `20`; unknown avg `0.1497` n `979`
- 24h: commodity avg `-0.2062` n `13`; crypto_alt avg `0.5248` n `235`; crypto_major avg `0.1675` n `8`; equity avg `0.2579` n `144`; fx avg `-0.0837` n `6`; index avg `0.1166` n `26`; metal avg `0.0989` n `20`; unknown avg `630.2723` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal

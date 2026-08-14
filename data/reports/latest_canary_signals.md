# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T20:37:27.199468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `0.0052` n `8`; equity avg `0.0044` n `114`; fx avg `0.0021` n `6`; index avg `-0.0076` n `25`; metal avg `0.0139` n `20`; unknown avg `0.2703` n `791`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `0.0885` n `230`; crypto_major avg `0.1035` n `8`; equity avg `0.1519` n `114`; fx avg `0.0217` n `6`; index avg `0.0153` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.0489` n `791`
- 4h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.2409` n `230`; crypto_major avg `-0.3421` n `8`; equity avg `0.0894` n `114`; fx avg `0.0047` n `6`; index avg `0.0259` n `25`; metal avg `-0.0563` n `20`; unknown avg `-0.3597` n `791`
- 24h: commodity avg `0.1855` n `12`; crypto_alt avg `0.2656` n `230`; crypto_major avg `-1.0478` n `8`; equity avg `-0.4227` n `114`; fx avg `0.0928` n `6`; index avg `-0.0802` n `25`; metal avg `0.2215` n `20`; unknown avg `-0.0397` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal

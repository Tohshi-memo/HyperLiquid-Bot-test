# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T18:52:46.815098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `0.0064` n `230`; crypto_major avg `-0.0342` n `8`; equity avg `-0.0146` n `102`; fx avg `0.0002` n `6`; index avg `0.0243` n `25`; metal avg `-0.0363` n `20`; unknown avg `0.0506` n `779`
- 1h: commodity avg `-0.0908` n `12`; crypto_alt avg `-0.1462` n `230`; crypto_major avg `-0.1877` n `8`; equity avg `-0.197` n `102`; fx avg `0.0022` n `6`; index avg `0.0073` n `25`; metal avg `0.0223` n `20`; unknown avg `0.0663` n `779`
- 4h: commodity avg `-0.1195` n `12`; crypto_alt avg `-0.33` n `230`; crypto_major avg `0.2692` n `8`; equity avg `0.4021` n `102`; fx avg `-0.0787` n `6`; index avg `0.0783` n `25`; metal avg `0.2135` n `20`; unknown avg `-0.0397` n `779`
- 24h: commodity avg `-0.1627` n `12`; crypto_alt avg `-0.3933` n `230`; crypto_major avg `0.2839` n `8`; equity avg `2.4376` n `102`; fx avg `-0.3827` n `6`; index avg `0.0898` n `25`; metal avg `0.1721` n `20`; unknown avg `-0.1397` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal

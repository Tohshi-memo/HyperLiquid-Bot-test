# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T20:22:30.393637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `0.0514` n `8`; equity avg `-0.0948` n `94`; fx avg `-0.0007` n `6`; index avg `0.007` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.0062` n `768`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `0.0564` n `230`; crypto_major avg `0.0523` n `8`; equity avg `-0.0574` n `94`; fx avg `-0.0119` n `6`; index avg `0.0348` n `25`; metal avg `-0.0561` n `20`; unknown avg `0.0012` n `768`
- 4h: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.5199` n `230`; crypto_major avg `-0.7823` n `8`; equity avg `-0.461` n `94`; fx avg `-0.0129` n `6`; index avg `-0.1028` n `25`; metal avg `-0.2092` n `20`; unknown avg `-0.2487` n `768`
- 24h: commodity avg `-0.3218` n `12`; crypto_alt avg `-1.1378` n `230`; crypto_major avg `-2.0612` n `8`; equity avg `-3.8563` n `94`; fx avg `-0.1639` n `6`; index avg `-0.5469` n `25`; metal avg `-0.8625` n `20`; unknown avg `-0.2866` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal

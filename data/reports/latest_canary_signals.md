# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T22:52:24.198049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.174` n `230`; crypto_major avg `0.1767` n `8`; equity avg `0.0155` n `96`; fx avg `0.0015` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0628` n `770`
- 1h: commodity avg `0.0458` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `0.1426` n `8`; equity avg `-0.0307` n `96`; fx avg `-0.0001` n `6`; index avg `0.0088` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.161` n `770`
- 4h: commodity avg `-0.0847` n `12`; crypto_alt avg `0.3801` n `230`; crypto_major avg `0.3428` n `8`; equity avg `-0.0039` n `96`; fx avg `0.017` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.4295` n `770`
- 24h: commodity avg `0.3108` n `12`; crypto_alt avg `-0.1924` n `230`; crypto_major avg `0.6975` n `8`; equity avg `-0.2596` n `96`; fx avg `-0.0687` n `6`; index avg `0.0421` n `25`; metal avg `-0.042` n `20`; unknown avg `0.2163` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal

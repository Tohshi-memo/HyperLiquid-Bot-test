# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T23:52:27.189185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.1253` n `230`; crypto_major avg `-0.0653` n `8`; equity avg `-0.0612` n `94`; fx avg `0.0171` n `6`; index avg `-0.0197` n `25`; metal avg `-0.009` n `20`; unknown avg `0.1002` n `768`
- 1h: commodity avg `-0.055` n `12`; crypto_alt avg `-0.1836` n `230`; crypto_major avg `-0.1701` n `8`; equity avg `0.0403` n `94`; fx avg `0.0028` n `6`; index avg `0.0148` n `25`; metal avg `0.0028` n `20`; unknown avg `0.7273` n `768`
- 4h: commodity avg `-0.1032` n `12`; crypto_alt avg `0.1835` n `230`; crypto_major avg `0.1285` n `8`; equity avg `-0.1697` n `94`; fx avg `-0.0017` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0141` n `20`; unknown avg `0.1535` n `768`
- 24h: commodity avg `0.0848` n `12`; crypto_alt avg `0.0776` n `230`; crypto_major avg `0.2612` n `8`; equity avg `-1.028` n `93`; fx avg `0.2181` n `6`; index avg `-0.2654` n `25`; metal avg `0.108` n `20`; unknown avg `0.0056` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T12:07:34.222424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.1242` n `234`; crypto_major avg `-0.165` n `8`; equity avg `-0.0029` n `137`; fx avg `-0.0018` n `6`; index avg `0.0111` n `27`; metal avg `-0.0208` n `20`; unknown avg `0.0041` n `917`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.3226` n `234`; crypto_major avg `0.3798` n `8`; equity avg `0.2172` n `137`; fx avg `-0.0295` n `6`; index avg `0.0393` n `27`; metal avg `-0.0053` n `20`; unknown avg `9.6877` n `917`
- 4h: commodity avg `-0.0586` n `12`; crypto_alt avg `0.9273` n `234`; crypto_major avg `1.0915` n `8`; equity avg `0.5209` n `137`; fx avg `-0.019` n `6`; index avg `0.1056` n `27`; metal avg `0.1317` n `20`; unknown avg `0.2263` n `911`
- 24h: commodity avg `0.1824` n `12`; crypto_alt avg `-2.3113` n `234`; crypto_major avg `-2.2122` n `8`; equity avg `0.0043` n `137`; fx avg `0.0721` n `6`; index avg `0.0948` n `27`; metal avg `0.5051` n `20`; unknown avg `18890.7778` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal

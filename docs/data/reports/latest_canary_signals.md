# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T20:22:35.229411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0772` n `12`; crypto_alt avg `-0.0971` n `234`; crypto_major avg `-0.1123` n `8`; equity avg `-0.1106` n `141`; fx avg `-0.0072` n `6`; index avg `-0.0335` n `26`; metal avg `-0.068` n `20`; unknown avg `2.2373` n `908`
- 1h: commodity avg `-0.186` n `12`; crypto_alt avg `-0.0816` n `234`; crypto_major avg `-0.2717` n `8`; equity avg `-0.2462` n `141`; fx avg `-0.0183` n `6`; index avg `-0.0442` n `26`; metal avg `-0.0617` n `20`; unknown avg `4.9604` n `870`
- 4h: commodity avg `0.0852` n `12`; crypto_alt avg `-0.0685` n `234`; crypto_major avg `-0.1762` n `8`; equity avg `-0.1274` n `141`; fx avg `-0.0082` n `6`; index avg `-0.0762` n `26`; metal avg `-0.0733` n `20`; unknown avg `12.6039` n `869`
- 24h: commodity avg `0.7901` n `12`; crypto_alt avg `4.0477` n `234`; crypto_major avg `1.5657` n `8`; equity avg `-0.3806` n `141`; fx avg `0.0312` n `6`; index avg `-0.1351` n `26`; metal avg `-0.1201` n `20`; unknown avg `11.5314` n `847`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal

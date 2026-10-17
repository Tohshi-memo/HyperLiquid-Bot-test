# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T11:37:27.471740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `13`; crypto_alt avg `-0.0152` n `236`; crypto_major avg `0.0129` n `8`; equity avg `-0.0037` n `151`; fx avg `0.0024` n `6`; index avg `-0.004` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.0672` n `1193`
- 1h: commodity avg `-0.0208` n `13`; crypto_alt avg `-0.2123` n `236`; crypto_major avg `-0.1283` n `8`; equity avg `-0.0037` n `151`; fx avg `-0.0057` n `6`; index avg `0.0221` n `26`; metal avg `0.0074` n `20`; unknown avg `-0.0011` n `1191`
- 4h: commodity avg `0.0407` n `13`; crypto_alt avg `-0.4393` n `236`; crypto_major avg `-0.3339` n `8`; equity avg `0.015` n `151`; fx avg `-0.0` n `6`; index avg `0.0299` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.1744` n `1173`
- 24h: commodity avg `0.2792` n `13`; crypto_alt avg `-2.8755` n `236`; crypto_major avg `-2.0925` n `8`; equity avg `-3.3467` n `151`; fx avg `-0.0032` n `6`; index avg `-0.5084` n `26`; metal avg `-0.2314` n `20`; unknown avg `8.9838` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1853`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.151`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal

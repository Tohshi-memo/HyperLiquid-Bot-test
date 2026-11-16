# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T04:52:24.860525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `-0.2187` n `239`; crypto_major avg `-0.2957` n `8`; equity avg `-0.311` n `162`; fx avg `-0.0128` n `6`; index avg `-0.043` n `27`; metal avg `-0.0379` n `20`; unknown avg `3.1878` n `1265`
- 1h: commodity avg `0.0719` n `13`; crypto_alt avg `-0.0852` n `239`; crypto_major avg `-0.3356` n `8`; equity avg `-0.2814` n `162`; fx avg `-0.0186` n `6`; index avg `-0.0378` n `27`; metal avg `-0.0581` n `20`; unknown avg `-0.1432` n `1255`
- 4h: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.2229` n `239`; crypto_major avg `-0.5824` n `8`; equity avg `-1.6445` n `162`; fx avg `-0.0219` n `6`; index avg `-0.228` n `27`; metal avg `-0.4025` n `20`; unknown avg `0.3682` n `1239`
- 24h: commodity avg `-0.3496` n `13`; crypto_alt avg `-0.3516` n `239`; crypto_major avg `-0.4107` n `8`; equity avg `-0.1986` n `162`; fx avg `-0.037` n `6`; index avg `-0.0188` n `27`; metal avg `0.1393` n `20`; unknown avg `1.0222` n `1131`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal

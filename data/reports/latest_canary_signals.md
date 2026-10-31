# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T15:22:23.983081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `0.3079` n `238`; crypto_major avg `0.1588` n `8`; equity avg `0.0171` n `156`; fx avg `0.0028` n `6`; index avg `-0.0016` n `27`; metal avg `0.0071` n `20`; unknown avg `0.2807` n `1262`
- 1h: commodity avg `-0.0249` n `13`; crypto_alt avg `0.572` n `238`; crypto_major avg `0.166` n `8`; equity avg `0.0649` n `156`; fx avg `0.0145` n `6`; index avg `0.0035` n `27`; metal avg `0.0101` n `20`; unknown avg `-0.1156` n `1256`
- 4h: commodity avg `-0.1204` n `13`; crypto_alt avg `0.6577` n `238`; crypto_major avg `0.0564` n `8`; equity avg `0.0547` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0033` n `27`; metal avg `0.0185` n `20`; unknown avg `200.0553` n `1248`
- 24h: commodity avg `-0.3691` n `13`; crypto_alt avg `0.2707` n `238`; crypto_major avg `-0.9498` n `8`; equity avg `-0.306` n `156`; fx avg `0.0358` n `6`; index avg `-0.1057` n `27`; metal avg `-0.0523` n `20`; unknown avg `0.9365` n `1097`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal

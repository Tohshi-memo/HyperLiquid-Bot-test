# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T02:22:16.207716+00:00`
- Correlation status: `ready`
- Asset price records: `509`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1876` n `12`; crypto_alt avg `-0.1769` n `228`; crypto_major avg `-0.1068` n `8`; equity avg `-0.1265` n `65`; fx avg `0.0186` n `4`; index avg `-0.0362` n `23`; metal avg `-0.3233` n `18`; unknown avg `-0.1777` n `358`
- 1h: commodity avg `-0.0965` n `12`; crypto_alt avg `-0.1211` n `228`; crypto_major avg `-0.2295` n `8`; equity avg `0.163` n `65`; fx avg `0.012` n `4`; index avg `0.0599` n `23`; metal avg `-0.2501` n `18`; unknown avg `-0.2897` n `357`
- 4h: commodity avg `-0.0886` n `12`; crypto_alt avg `-1.128` n `228`; crypto_major avg `-0.9104` n `8`; equity avg `0.0345` n `65`; fx avg `0.0904` n `4`; index avg `0.1085` n `23`; metal avg `0.1475` n `18`; unknown avg `-0.7414` n `356`
- 24h: commodity avg `-1.7381` n `7`; crypto_alt avg `-0.0915` n `223`; crypto_major avg `-1.1348` n `7`; equity avg `1.5693` n `47`; fx avg `-0.2514` n `4`; index avg `1.0751` n `6`; metal avg `2.0357` n `7`; unknown avg `2.31` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1403`, n `505`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `505`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `505`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0775`, n `501`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `505`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0703`, n `501`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `501`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `501`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `505`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0643`, n `501`, weak_sample_signal

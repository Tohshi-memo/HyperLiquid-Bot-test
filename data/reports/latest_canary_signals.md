# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T15:37:31.227579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0784` n `13`; crypto_alt avg `0.0142` n `235`; crypto_major avg `-0.2099` n `8`; equity avg `-0.1591` n `150`; fx avg `0.0143` n `6`; index avg `-0.0173` n `26`; metal avg `0.0332` n `20`; unknown avg `1.0093` n `1076`
- 1h: commodity avg `0.0348` n `13`; crypto_alt avg `0.3331` n `235`; crypto_major avg `0.0937` n `8`; equity avg `0.2794` n `150`; fx avg `0.0302` n `6`; index avg `0.0501` n `26`; metal avg `0.1629` n `20`; unknown avg `-0.0641` n `1066`
- 4h: commodity avg `0.1958` n `13`; crypto_alt avg `0.1733` n `235`; crypto_major avg `0.0974` n `8`; equity avg `0.2689` n `150`; fx avg `0.0158` n `6`; index avg `0.0047` n `26`; metal avg `-0.0281` n `20`; unknown avg `4.5728` n `1018`
- 24h: commodity avg `-0.5161` n `13`; crypto_alt avg `0.8293` n `235`; crypto_major avg `0.7166` n `8`; equity avg `0.9254` n `149`; fx avg `0.1226` n `6`; index avg `0.1677` n `26`; metal avg `-0.0093` n `20`; unknown avg `381.3118` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal

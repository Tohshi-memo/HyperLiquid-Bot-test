# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T18:07:32.253508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `13`; crypto_alt avg `0.0279` n `235`; crypto_major avg `0.1632` n `8`; equity avg `0.0455` n `150`; fx avg `-0.0013` n `6`; index avg `0.0023` n `26`; metal avg `0.0187` n `20`; unknown avg `0.1163` n `1074`
- 1h: commodity avg `-0.0186` n `13`; crypto_alt avg `0.254` n `235`; crypto_major avg `0.197` n `8`; equity avg `0.2422` n `150`; fx avg `0.0068` n `6`; index avg `0.0117` n `26`; metal avg `0.0446` n `20`; unknown avg `-0.0637` n `1074`
- 4h: commodity avg `0.2798` n `13`; crypto_alt avg `-0.0282` n `235`; crypto_major avg `-0.2642` n `8`; equity avg `-0.0645` n `150`; fx avg `0.0168` n `6`; index avg `-0.0831` n `26`; metal avg `0.172` n `20`; unknown avg `5.6733` n `1018`
- 24h: commodity avg `-0.1043` n `13`; crypto_alt avg `0.0241` n `235`; crypto_major avg `-0.0291` n `8`; equity avg `0.7943` n `149`; fx avg `0.1135` n `6`; index avg `0.0614` n `26`; metal avg `0.0416` n `20`; unknown avg `381.9421` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal

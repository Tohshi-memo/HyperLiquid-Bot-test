# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T20:38:00.594273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.1254` n `230`; crypto_major avg `0.1636` n `8`; equity avg `-0.208` n `107`; fx avg `-0.0006` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0076` n `782`
- 1h: commodity avg `-0.0983` n `12`; crypto_alt avg `-0.021` n `230`; crypto_major avg `-0.0408` n `8`; equity avg `-0.9284` n `107`; fx avg `-0.0037` n `6`; index avg `-0.1029` n `25`; metal avg `-0.0397` n `20`; unknown avg `0.0352` n `782`
- 4h: commodity avg `-0.1408` n `12`; crypto_alt avg `0.4136` n `230`; crypto_major avg `0.328` n `8`; equity avg `-0.5114` n `107`; fx avg `0.0504` n `6`; index avg `0.065` n `25`; metal avg `-0.1422` n `20`; unknown avg `-0.1027` n `782`
- 24h: commodity avg `-1.2284` n `12`; crypto_alt avg `-0.1166` n `230`; crypto_major avg `0.2695` n `8`; equity avg `2.7951` n `107`; fx avg `0.1278` n `6`; index avg `0.6926` n `25`; metal avg `0.8265` n `20`; unknown avg `0.4263` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T20:37:28.223488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.0122` n `230`; crypto_major avg `-0.0605` n `8`; equity avg `0.0417` n `102`; fx avg `0.0035` n `6`; index avg `-0.0042` n `25`; metal avg `0.02` n `20`; unknown avg `-0.0133` n `783`
- 1h: commodity avg `0.0981` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.0095` n `8`; equity avg `0.0802` n `102`; fx avg `0.015` n `6`; index avg `0.0198` n `25`; metal avg `0.0321` n `20`; unknown avg `-0.0928` n `783`
- 4h: commodity avg `0.0668` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `0.4445` n `8`; equity avg `0.46` n `102`; fx avg `0.0887` n `6`; index avg `0.0547` n `25`; metal avg `0.0988` n `20`; unknown avg `0.1409` n `782`
- 24h: commodity avg `-1.2546` n `12`; crypto_alt avg `1.4814` n `230`; crypto_major avg `1.9132` n `8`; equity avg `1.8033` n `102`; fx avg `-0.0325` n `6`; index avg `0.3421` n `25`; metal avg `0.3857` n `20`; unknown avg `1.6218` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal

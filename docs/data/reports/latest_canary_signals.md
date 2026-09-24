# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T10:37:31.864062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7596` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.104` n `234`; crypto_major avg `-0.0293` n `8`; equity avg `0.0837` n `141`; fx avg `0.0191` n `6`; index avg `0.0069` n `26`; metal avg `0.0777` n `20`; unknown avg `0.2293` n `945`
- 1h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.404` n `234`; crypto_major avg `-0.4093` n `8`; equity avg `0.2337` n `141`; fx avg `0.0013` n `6`; index avg `0.0142` n `26`; metal avg `0.0236` n `20`; unknown avg `1.1874` n `943`
- 4h: commodity avg `0.0837` n `12`; crypto_alt avg `-2.0648` n `234`; crypto_major avg `-1.8511` n `8`; equity avg `-0.5733` n `141`; fx avg `0.0246` n `6`; index avg `-0.0915` n `26`; metal avg `-0.1362` n `20`; unknown avg `2.0126` n `937`
- 24h: commodity avg `0.6495` n `12`; crypto_alt avg `-5.4495` n `234`; crypto_major avg `-4.4128` n `8`; equity avg `-2.5494` n `141`; fx avg `0.0443` n `6`; index avg `-0.4861` n `26`; metal avg `-0.4955` n `20`; unknown avg `586.7241` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal

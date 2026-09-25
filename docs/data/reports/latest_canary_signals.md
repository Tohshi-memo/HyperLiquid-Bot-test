# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T12:22:41.864748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0865` n `12`; crypto_alt avg `-0.7261` n `234`; crypto_major avg `-0.767` n `8`; equity avg `-0.0979` n `141`; fx avg `0.0088` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0027` n `20`; unknown avg `3.883` n `944`
- 1h: commodity avg `0.0766` n `12`; crypto_alt avg `-0.6675` n `234`; crypto_major avg `-0.5748` n `8`; equity avg `-0.155` n `141`; fx avg `0.0251` n `6`; index avg `-0.024` n `26`; metal avg `-0.0126` n `20`; unknown avg `3.7165` n `936`
- 4h: commodity avg `-0.1557` n `12`; crypto_alt avg `0.5893` n `234`; crypto_major avg `0.8436` n `8`; equity avg `0.0631` n `141`; fx avg `-0.0336` n `6`; index avg `0.0351` n `26`; metal avg `0.2257` n `20`; unknown avg `3.0529` n `936`
- 24h: commodity avg `0.1092` n `12`; crypto_alt avg `4.667` n `234`; crypto_major avg `2.9537` n `8`; equity avg `1.6249` n `141`; fx avg `-0.1988` n `6`; index avg `0.269` n `26`; metal avg `0.1988` n `20`; unknown avg `12.5857` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal

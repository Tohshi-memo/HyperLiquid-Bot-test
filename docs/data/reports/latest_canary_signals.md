# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T07:22:25.117308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `13`; crypto_alt avg `0.0927` n `239`; crypto_major avg `0.0545` n `8`; equity avg `0.0138` n `158`; fx avg `0.0006` n `6`; index avg `0.0028` n `27`; metal avg `0.0013` n `20`; unknown avg `0.0334` n `1259`
- 1h: commodity avg `0.0267` n `13`; crypto_alt avg `0.2375` n `239`; crypto_major avg `0.0418` n `8`; equity avg `-0.0111` n `158`; fx avg `0.0024` n `6`; index avg `0.0089` n `27`; metal avg `-0.0014` n `20`; unknown avg `11.6103` n `1249`
- 4h: commodity avg `-0.0641` n `13`; crypto_alt avg `0.1667` n `239`; crypto_major avg `0.0594` n `8`; equity avg `-0.1255` n `158`; fx avg `-0.0078` n `6`; index avg `0.0188` n `27`; metal avg `-0.0123` n `20`; unknown avg `12.1942` n `1203`
- 24h: commodity avg `-0.2959` n `13`; crypto_alt avg `0.6509` n `239`; crypto_major avg `0.7437` n `8`; equity avg `1.3879` n `158`; fx avg `0.0093` n `6`; index avg `0.2419` n `27`; metal avg `0.2525` n `20`; unknown avg `8.7105` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal

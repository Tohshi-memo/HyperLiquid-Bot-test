# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T12:22:58.595375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0944` n `12`; crypto_alt avg `0.3938` n `234`; crypto_major avg `0.2702` n `8`; equity avg `0.1641` n `141`; fx avg `0.0043` n `6`; index avg `0.0249` n `26`; metal avg `0.0784` n `20`; unknown avg `0.7607` n `945`
- 1h: commodity avg `-0.1065` n `12`; crypto_alt avg `0.073` n `234`; crypto_major avg `0.1139` n `8`; equity avg `0.0199` n `141`; fx avg `-0.0246` n `6`; index avg `0.0076` n `26`; metal avg `0.0474` n `20`; unknown avg `4.2148` n `937`
- 4h: commodity avg `-0.2385` n `12`; crypto_alt avg `-0.9054` n `234`; crypto_major avg `-0.912` n `8`; equity avg `0.0353` n `141`; fx avg `-0.0239` n `6`; index avg `0.0256` n `26`; metal avg `0.0543` n `20`; unknown avg `0.3331` n `937`
- 24h: commodity avg `0.3592` n `12`; crypto_alt avg `-3.9255` n `234`; crypto_major avg `-3.1659` n `8`; equity avg `-1.798` n `141`; fx avg `0.0045` n `6`; index avg `-0.3588` n `26`; metal avg `-0.3104` n `20`; unknown avg `587.5185` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T09:22:32.550207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1102` n `13`; crypto_alt avg `0.1517` n `239`; crypto_major avg `0.2168` n `8`; equity avg `0.2994` n `158`; fx avg `-0.0147` n `6`; index avg `0.0306` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.0736` n `1256`
- 1h: commodity avg `-0.2121` n `13`; crypto_alt avg `0.3401` n `239`; crypto_major avg `0.5171` n `8`; equity avg `1.307` n `158`; fx avg `-0.0109` n `6`; index avg `0.1615` n `27`; metal avg `0.0779` n `20`; unknown avg `30.4969` n `1250`
- 4h: commodity avg `-0.235` n `13`; crypto_alt avg `1.002` n `239`; crypto_major avg `0.7137` n `8`; equity avg `1.7487` n `158`; fx avg `-0.135` n `6`; index avg `0.1911` n `27`; metal avg `0.3676` n `20`; unknown avg `18.8073` n `1170`
- 24h: commodity avg `0.7285` n `13`; crypto_alt avg `-3.7659` n `239`; crypto_major avg `-5.361` n `8`; equity avg `-4.5107` n `158`; fx avg `-0.0547` n `6`; index avg `-0.5847` n `27`; metal avg `-0.1746` n `20`; unknown avg `232.4425` n `1047`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2201`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal

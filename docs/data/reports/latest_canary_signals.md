# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T09:22:30.873459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1525` n `13`; crypto_alt avg `-0.098` n `239`; crypto_major avg `-0.0997` n `8`; equity avg `0.0102` n `158`; fx avg `0.0166` n `6`; index avg `0.022` n `27`; metal avg `0.0719` n `20`; unknown avg `16.52` n `1254`
- 1h: commodity avg `-0.084` n `13`; crypto_alt avg `-0.3806` n `239`; crypto_major avg `-0.1241` n `8`; equity avg `-0.1948` n `158`; fx avg `0.0594` n `6`; index avg `0.0306` n `27`; metal avg `0.1094` n `20`; unknown avg `17.6117` n `1182`
- 4h: commodity avg `-0.1183` n `13`; crypto_alt avg `1.4589` n `239`; crypto_major avg `1.0591` n `8`; equity avg `1.7354` n `158`; fx avg `0.1107` n `6`; index avg `0.2596` n `27`; metal avg `0.8939` n `20`; unknown avg `18.5163` n `1148`
- 24h: commodity avg `-0.4745` n `13`; crypto_alt avg `2.382` n `239`; crypto_major avg `1.4544` n `8`; equity avg `2.0015` n `158`; fx avg `0.1661` n `6`; index avg `0.1616` n `27`; metal avg `1.1232` n `20`; unknown avg `1.0065` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2465`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal

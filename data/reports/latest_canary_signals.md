# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T14:07:45.691504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7681` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `3.4036` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9798` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `2.8048` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2638` n `13`; crypto_alt avg `2.5953` n `239`; crypto_major avg `3.5965` n `8`; equity avg `5.1916` n `166`; fx avg `0.0036` n `6`; index avg `0.6142` n `27`; metal avg `0.7383` n `20`; unknown avg `133.8979` n `1258`
- 1h: commodity avg `-0.0144` n `13`; crypto_alt avg `2.4101` n `239`; crypto_major avg `3.3892` n `8`; equity avg `4.8047` n `166`; fx avg `-0.0773` n `6`; index avg `0.5416` n `27`; metal avg `0.5844` n `20`; unknown avg `176.559` n `1262`
- 4h: commodity avg `-0.2948` n `13`; crypto_alt avg `2.1947` n `239`; crypto_major avg `3.4733` n `8`; equity avg `4.2755` n `166`; fx avg `-0.1414` n `6`; index avg `0.5078` n `27`; metal avg `0.4935` n `20`; unknown avg `16.3442` n `1252`
- 24h: commodity avg `-1.0084` n `13`; crypto_alt avg `2.7677` n `239`; crypto_major avg `4.653` n `8`; equity avg `6.5842` n `166`; fx avg `0.063` n `6`; index avg `0.5826` n `27`; metal avg `0.9074` n `20`; unknown avg `14.9754` n `1059`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal

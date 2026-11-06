# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T12:37:27.444183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0732` n `13`; crypto_alt avg `-0.152` n `239`; crypto_major avg `-0.086` n `8`; equity avg `0.0695` n `158`; fx avg `-0.0232` n `6`; index avg `-0.002` n `27`; metal avg `-0.014` n `20`; unknown avg `0.4483` n `1257`
- 1h: commodity avg `-0.1277` n `13`; crypto_alt avg `-0.0465` n `239`; crypto_major avg `0.0972` n `8`; equity avg `0.1591` n `158`; fx avg `0.0207` n `6`; index avg `0.0033` n `27`; metal avg `-0.0125` n `20`; unknown avg `-0.0808` n `1187`
- 4h: commodity avg `0.0396` n `13`; crypto_alt avg `0.9423` n `239`; crypto_major avg `0.8174` n `8`; equity avg `1.7797` n `158`; fx avg `0.0645` n `6`; index avg `0.1662` n `27`; metal avg `0.0136` n `20`; unknown avg `33.2147` n `1174`
- 24h: commodity avg `0.5551` n `13`; crypto_alt avg `-2.0603` n `239`; crypto_major avg `-4.3682` n `8`; equity avg `-3.4755` n `158`; fx avg `0.0135` n `6`; index avg `-0.5496` n `27`; metal avg `-0.245` n `20`; unknown avg `14.1851` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal

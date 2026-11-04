# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T08:37:26.193285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.0067` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0773` n `13`; crypto_alt avg `0.0467` n `239`; crypto_major avg `0.0625` n `8`; equity avg `-0.0765` n `158`; fx avg `0.0041` n `6`; index avg `0.0052` n `27`; metal avg `0.0191` n `20`; unknown avg `-0.0851` n `1232`
- 1h: commodity avg `-0.0017` n `13`; crypto_alt avg `0.3836` n `239`; crypto_major avg `0.3975` n `8`; equity avg `0.5171` n `158`; fx avg `-0.0023` n `6`; index avg `0.0895` n `27`; metal avg `0.0766` n `20`; unknown avg `-0.0289` n `1212`
- 4h: commodity avg `0.3749` n `13`; crypto_alt avg `3.3927` n `239`; crypto_major avg `2.3816` n `8`; equity avg `3.7534` n `158`; fx avg `0.0818` n `6`; index avg `0.5801` n `27`; metal avg `1.0745` n `20`; unknown avg `4.0457` n `1194`
- 24h: commodity avg `-0.3322` n `13`; crypto_alt avg `3.5072` n `239`; crypto_major avg `2.1667` n `8`; equity avg `2.7988` n `158`; fx avg `0.123` n `6`; index avg `0.2057` n `27`; metal avg `0.9868` n `20`; unknown avg `191.5703` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2348`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal

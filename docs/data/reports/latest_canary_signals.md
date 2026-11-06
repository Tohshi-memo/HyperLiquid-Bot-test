# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T01:52:31.940479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `13`; crypto_alt avg `0.0262` n `239`; crypto_major avg `0.0576` n `8`; equity avg `0.3356` n `158`; fx avg `-0.0084` n `6`; index avg `0.0615` n `27`; metal avg `-0.0056` n `20`; unknown avg `0.8958` n `1256`
- 1h: commodity avg `0.0971` n `13`; crypto_alt avg `0.0968` n `239`; crypto_major avg `-0.0485` n `8`; equity avg `0.3886` n `158`; fx avg `-0.0208` n `6`; index avg `0.0819` n `27`; metal avg `-0.0875` n `20`; unknown avg `16.0029` n `1254`
- 4h: commodity avg `0.0456` n `13`; crypto_alt avg `0.4175` n `239`; crypto_major avg `0.2622` n `8`; equity avg `1.1687` n `158`; fx avg `-0.0074` n `6`; index avg `0.1883` n `27`; metal avg `0.0063` n `20`; unknown avg `1.9895` n `1216`
- 24h: commodity avg `1.2464` n `13`; crypto_alt avg `-4.8018` n `239`; crypto_major avg `-5.6273` n `8`; equity avg `-6.6065` n `158`; fx avg `0.0463` n `6`; index avg `-0.9307` n `27`; metal avg `-0.3831` n `20`; unknown avg `231.7249` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2336`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal

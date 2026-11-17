# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T22:52:31.191214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `0.0374` n `239`; crypto_major avg `0.0416` n `8`; equity avg `0.2076` n `163`; fx avg `0.008` n `6`; index avg `0.0043` n `27`; metal avg `0.0107` n `20`; unknown avg `0.4016` n `1227`
- 1h: commodity avg `0.0021` n `13`; crypto_alt avg `0.562` n `239`; crypto_major avg `0.5054` n `8`; equity avg `1.3616` n `163`; fx avg `0.0257` n `6`; index avg `0.1255` n `27`; metal avg `0.041` n `20`; unknown avg `165.9988` n `1217`
- 4h: commodity avg `-0.1747` n `13`; crypto_alt avg `1.4381` n `239`; crypto_major avg `1.2427` n `8`; equity avg `2.6057` n `163`; fx avg `-0.0111` n `6`; index avg `0.2431` n `27`; metal avg `-0.0061` n `20`; unknown avg `417.3726` n `1193`
- 24h: commodity avg `0.3158` n `13`; crypto_alt avg `0.6141` n `239`; crypto_major avg `0.212` n `8`; equity avg `0.9755` n `163`; fx avg `0.0322` n `6`; index avg `0.0627` n `27`; metal avg `0.0063` n `20`; unknown avg `6.7986` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal

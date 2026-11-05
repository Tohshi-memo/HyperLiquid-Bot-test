# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T03:07:30.920813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `13`; crypto_alt avg `-0.1151` n `239`; crypto_major avg `-0.0706` n `8`; equity avg `-0.1041` n `158`; fx avg `0.0172` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0151` n `20`; unknown avg `8.9966` n `1259`
- 1h: commodity avg `0.1006` n `13`; crypto_alt avg `0.1343` n `239`; crypto_major avg `-0.2294` n `8`; equity avg `0.033` n `158`; fx avg `0.0122` n `6`; index avg `-0.0036` n `27`; metal avg `0.0072` n `20`; unknown avg `1.2914` n `1257`
- 4h: commodity avg `-0.2437` n `13`; crypto_alt avg `-0.0041` n `239`; crypto_major avg `-0.0632` n `8`; equity avg `-0.7698` n `158`; fx avg `0.0217` n `6`; index avg `-0.2052` n `27`; metal avg `0.4835` n `20`; unknown avg `161.0251` n `1248`
- 24h: commodity avg `-1.631` n `13`; crypto_alt avg `4.6756` n `239`; crypto_major avg `4.9596` n `8`; equity avg `1.4619` n `158`; fx avg `0.1385` n `6`; index avg `0.5726` n `27`; metal avg `2.038` n `20`; unknown avg `33.5135` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2532`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal

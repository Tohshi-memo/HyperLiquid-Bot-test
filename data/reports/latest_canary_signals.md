# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T09:52:30.903860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0307` n `13`; crypto_alt avg `0.0654` n `239`; crypto_major avg `0.0875` n `8`; equity avg `0.1007` n `158`; fx avg `-0.0107` n `6`; index avg `-0.0049` n `27`; metal avg `0.0104` n `20`; unknown avg `0.1506` n `1264`
- 1h: commodity avg `-0.0909` n `13`; crypto_alt avg `-0.2246` n `239`; crypto_major avg `-0.0592` n `8`; equity avg `0.3218` n `158`; fx avg `0.0425` n `6`; index avg `0.0893` n `27`; metal avg `0.0835` n `20`; unknown avg `24.802` n `1236`
- 4h: commodity avg `0.0277` n `13`; crypto_alt avg `0.6172` n `239`; crypto_major avg `0.594` n `8`; equity avg `1.3408` n `158`; fx avg `0.1041` n `6`; index avg `0.2295` n `27`; metal avg `0.4014` n `20`; unknown avg `26.6379` n `1148`
- 24h: commodity avg `-0.3204` n `13`; crypto_alt avg `2.5611` n `239`; crypto_major avg `1.5887` n `8`; equity avg `2.3484` n `158`; fx avg `0.1569` n `6`; index avg `0.2069` n `27`; metal avg `1.1059` n `20`; unknown avg `1.0698` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2548`, n `668`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal

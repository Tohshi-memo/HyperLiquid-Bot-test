# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T18:37:32.769186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0415` n `13`; crypto_alt avg `-0.0418` n `239`; crypto_major avg `-0.0103` n `8`; equity avg `-0.1098` n `161`; fx avg `0.0103` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.0005` n `1262`
- 1h: commodity avg `-0.0733` n `13`; crypto_alt avg `-0.3711` n `239`; crypto_major avg `-0.0747` n `8`; equity avg `-0.2334` n `161`; fx avg `0.0328` n `6`; index avg `-0.0158` n `27`; metal avg `-0.08` n `20`; unknown avg `-0.0396` n `1256`
- 4h: commodity avg `-0.1861` n `13`; crypto_alt avg `0.2375` n `239`; crypto_major avg `1.165` n `8`; equity avg `2.2086` n `161`; fx avg `0.0421` n `6`; index avg `0.2364` n `27`; metal avg `-0.2047` n `20`; unknown avg `-0.2844` n `1243`
- 24h: commodity avg `0.4316` n `13`; crypto_alt avg `0.7443` n `239`; crypto_major avg `1.6341` n `8`; equity avg `6.5412` n `161`; fx avg `-0.1268` n `6`; index avg `0.6233` n `27`; metal avg `0.0929` n `20`; unknown avg `4.8101` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal

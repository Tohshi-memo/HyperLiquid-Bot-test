# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T13:07:29.000014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1201` n `13`; crypto_alt avg `-0.067` n `239`; crypto_major avg `-0.0167` n `8`; equity avg `0.1183` n `162`; fx avg `0.0178` n `6`; index avg `0.015` n `27`; metal avg `0.0623` n `20`; unknown avg `0.1545` n `1256`
- 1h: commodity avg `-0.078` n `13`; crypto_alt avg `-0.0785` n `239`; crypto_major avg `-0.1269` n `8`; equity avg `-0.5294` n `162`; fx avg `0.0108` n `6`; index avg `-0.0385` n `27`; metal avg `0.0162` n `20`; unknown avg `0.0148` n `1260`
- 4h: commodity avg `-0.0667` n `13`; crypto_alt avg `0.4343` n `239`; crypto_major avg `0.9648` n `8`; equity avg `0.3484` n `162`; fx avg `-0.0021` n `6`; index avg `0.046` n `27`; metal avg `0.0431` n `20`; unknown avg `279.8979` n `1200`
- 24h: commodity avg `0.7692` n `13`; crypto_alt avg `0.2448` n `239`; crypto_major avg `-1.3207` n `8`; equity avg `-0.2687` n `162`; fx avg `0.0039` n `6`; index avg `0.0797` n `27`; metal avg `-0.3013` n `20`; unknown avg `2.5724` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal

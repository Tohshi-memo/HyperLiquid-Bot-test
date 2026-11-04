# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T04:22:27.243168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.61` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0338` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `0.2889` n `239`; crypto_major avg `0.0739` n `8`; equity avg `0.0504` n `158`; fx avg `0.0014` n `6`; index avg `0.02` n `27`; metal avg `-0.0135` n `20`; unknown avg `-0.0733` n `1264`
- 1h: commodity avg `-0.072` n `13`; crypto_alt avg `0.7812` n `239`; crypto_major avg `0.6618` n `8`; equity avg `-0.1619` n `158`; fx avg `-0.0034` n `6`; index avg `0.008` n `27`; metal avg `0.0118` n `20`; unknown avg `0.5808` n `1252`
- 4h: commodity avg `-0.3774` n `13`; crypto_alt avg `-0.5354` n `239`; crypto_major avg `-0.6201` n `8`; equity avg `-2.6539` n `158`; fx avg `-0.0813` n `6`; index avg `-0.4726` n `27`; metal avg `-0.2229` n `20`; unknown avg `0.6444` n `1254`
- 24h: commodity avg `-0.2031` n `13`; crypto_alt avg `0.0963` n `239`; crypto_major avg `-0.254` n `8`; equity avg `-0.7974` n `158`; fx avg `0.1074` n `6`; index avg `-0.3063` n `27`; metal avg `-0.3527` n `20`; unknown avg `-0.368` n `1049`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal

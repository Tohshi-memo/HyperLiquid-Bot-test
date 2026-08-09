# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T09:37:30.125910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `0.0198` n `8`; equity avg `-0.0014` n `112`; fx avg `-0.0007` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0101` n `785`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.1327` n `230`; crypto_major avg `-0.128` n `8`; equity avg `-0.1081` n `112`; fx avg `0.0001` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0085` n `785`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.0925` n `8`; equity avg `-0.018` n `112`; fx avg `-0.0144` n `6`; index avg `-0.0107` n `25`; metal avg `0.0196` n `20`; unknown avg `-0.0375` n `752`
- 24h: commodity avg `0.3257` n `12`; crypto_alt avg `1.1386` n `230`; crypto_major avg `0.2195` n `8`; equity avg `0.4781` n `112`; fx avg `-0.0237` n `6`; index avg `0.0583` n `25`; metal avg `0.0107` n `20`; unknown avg `0.317` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0442`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0427`, n `668`, weak_sample_signal

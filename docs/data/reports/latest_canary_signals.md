# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T06:52:23.849921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.1042` n `231`; crypto_major avg `0.3219` n `8`; equity avg `-0.0028` n `122`; fx avg `0.0036` n `6`; index avg `-0.0123` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0271` n `793`
- 1h: commodity avg `-0.0901` n `12`; crypto_alt avg `-0.0878` n `231`; crypto_major avg `0.3879` n `8`; equity avg `-0.0397` n `122`; fx avg `0.0218` n `6`; index avg `-0.0307` n `25`; metal avg `0.1234` n `20`; unknown avg `-0.015` n `777`
- 4h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0044` n `231`; crypto_major avg `0.0693` n `8`; equity avg `-0.6723` n `122`; fx avg `0.0189` n `6`; index avg `-0.1354` n `25`; metal avg `0.1653` n `20`; unknown avg `-0.0329` n `777`
- 24h: commodity avg `-0.3628` n `12`; crypto_alt avg `3.9632` n `231`; crypto_major avg `2.0833` n `8`; equity avg `-1.1612` n `122`; fx avg `-0.13` n `6`; index avg `-0.1301` n `25`; metal avg `0.2654` n `20`; unknown avg `5.5567` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal

# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T18:52:27.292085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.7283` n `230`; crypto_major avg `-0.6018` n `8`; equity avg `0.0949` n `121`; fx avg `0.001` n `6`; index avg `0.0096` n `25`; metal avg `0.0112` n `20`; unknown avg `0.1198` n `793`
- 1h: commodity avg `-0.0405` n `12`; crypto_alt avg `-0.7063` n `230`; crypto_major avg `-0.676` n `8`; equity avg `-0.0849` n `121`; fx avg `0.0083` n `6`; index avg `-0.0042` n `25`; metal avg `0.0343` n `20`; unknown avg `0.1162` n `793`
- 4h: commodity avg `0.0531` n `12`; crypto_alt avg `-0.7836` n `230`; crypto_major avg `-0.8798` n `8`; equity avg `0.1224` n `121`; fx avg `0.0364` n `6`; index avg `0.0316` n `25`; metal avg `0.1468` n `20`; unknown avg `0.0695` n `793`
- 24h: commodity avg `0.1329` n `12`; crypto_alt avg `6.8748` n `230`; crypto_major avg `4.4784` n `8`; equity avg `1.3587` n `121`; fx avg `-0.097` n `6`; index avg `0.1527` n `25`; metal avg `0.6231` n `20`; unknown avg `1.1343` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal

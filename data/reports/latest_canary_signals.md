# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T09:07:27.897982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `0.0882` n `234`; crypto_major avg `0.1682` n `8`; equity avg `0.1267` n `142`; fx avg `0.0184` n `6`; index avg `0.053` n `26`; metal avg `0.0238` n `20`; unknown avg `0.2945` n `973`
- 1h: commodity avg `-0.0513` n `13`; crypto_alt avg `0.2359` n `234`; crypto_major avg `0.277` n `8`; equity avg `-0.0159` n `142`; fx avg `-0.0421` n `6`; index avg `0.0177` n `26`; metal avg `-0.1224` n `20`; unknown avg `0.3499` n `973`
- 4h: commodity avg `0.8107` n `13`; crypto_alt avg `-0.7995` n `234`; crypto_major avg `-0.6377` n `8`; equity avg `-0.5587` n `142`; fx avg `-0.0096` n `6`; index avg `-0.1579` n `26`; metal avg `-0.3988` n `20`; unknown avg `4.1376` n `930`
- 24h: commodity avg `0.0213` n `13`; crypto_alt avg `-0.0491` n `234`; crypto_major avg `0.5447` n `8`; equity avg `0.3216` n `142`; fx avg `0.0957` n `6`; index avg `0.0995` n `26`; metal avg `-0.424` n `20`; unknown avg `776.5369` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal

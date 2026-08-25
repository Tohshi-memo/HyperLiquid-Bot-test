# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T11:07:27.043241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5075` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3628` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1136` n `231`; crypto_major avg `-0.0657` n `8`; equity avg `-0.2231` n `122`; fx avg `-0.0001` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0328` n `20`; unknown avg `0.0405` n `795`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.042` n `231`; crypto_major avg `0.1268` n `8`; equity avg `-0.291` n `122`; fx avg `-0.0198` n `6`; index avg `-0.0419` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0908` n `795`
- 4h: commodity avg `-0.2973` n `12`; crypto_alt avg `-1.0799` n `231`; crypto_major avg `-1.3036` n `8`; equity avg `0.2039` n `122`; fx avg `-0.0243` n `6`; index avg `0.0592` n `25`; metal avg `-0.0839` n `20`; unknown avg `-0.0807` n `794`
- 24h: commodity avg `-0.6522` n `12`; crypto_alt avg `0.6714` n `231`; crypto_major avg `1.4625` n `8`; equity avg `0.8277` n `122`; fx avg `-0.0004` n `6`; index avg `0.1547` n `25`; metal avg `-0.203` n `20`; unknown avg `0.0349` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal

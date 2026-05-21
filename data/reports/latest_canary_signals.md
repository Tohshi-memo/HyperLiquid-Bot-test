# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T09:52:21.241475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0766` n `12`; crypto_alt avg `-0.0792` n `228`; crypto_major avg `-0.1625` n `8`; equity avg `-0.0789` n `66`; fx avg `0.0123` n `6`; index avg `-0.0436` n `23`; metal avg `-0.053` n `18`; unknown avg `-0.0233` n `386`
- 1h: commodity avg `-0.4919` n `12`; crypto_alt avg `-0.2941` n `228`; crypto_major avg `-0.2053` n `8`; equity avg `0.1256` n `66`; fx avg `0.031` n `6`; index avg `0.0989` n `23`; metal avg `0.1082` n `18`; unknown avg `0.0465` n `386`
- 4h: commodity avg `-0.6722` n `12`; crypto_alt avg `0.3702` n `228`; crypto_major avg `0.3307` n `8`; equity avg `0.1516` n `66`; fx avg `0.0024` n `6`; index avg `0.0248` n `23`; metal avg `0.276` n `18`; unknown avg `1.29` n `375`
- 24h: commodity avg `-2.3344` n `12`; crypto_alt avg `2.3721` n `228`; crypto_major avg `3.0707` n `8`; equity avg `1.7309` n `66`; fx avg `0.1134` n `6`; index avg `1.2431` n `23`; metal avg `0.366` n `18`; unknown avg `7.9877` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal

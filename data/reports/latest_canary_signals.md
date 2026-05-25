# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T03:52:21.604811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0988` n `12`; crypto_alt avg `0.0506` n `228`; crypto_major avg `0.0995` n `8`; equity avg `0.0364` n `67`; fx avg `0.0028` n `6`; index avg `0.1652` n `23`; metal avg `-0.1179` n `18`; unknown avg `-0.0689` n `397`
- 1h: commodity avg `-0.4896` n `12`; crypto_alt avg `0.0332` n `228`; crypto_major avg `-0.0995` n `8`; equity avg `0.1918` n `67`; fx avg `0.0059` n `6`; index avg `0.0012` n `23`; metal avg `-0.1102` n `18`; unknown avg `-0.0959` n `396`
- 4h: commodity avg `-0.4576` n `12`; crypto_alt avg `0.1701` n `228`; crypto_major avg `-0.535` n `8`; equity avg `0.3443` n `67`; fx avg `-0.1207` n `6`; index avg `0.1935` n `23`; metal avg `-0.4246` n `18`; unknown avg `-0.1349` n `396`
- 24h: commodity avg `-0.0876` n `12`; crypto_alt avg `-0.8593` n `228`; crypto_major avg `-0.1722` n `8`; equity avg `0.5067` n `67`; fx avg `-0.0516` n `6`; index avg `-0.2112` n `23`; metal avg `0.3588` n `18`; unknown avg `-0.5119` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal

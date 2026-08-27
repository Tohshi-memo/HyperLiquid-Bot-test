# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T07:07:25.185792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1307` n `12`; crypto_alt avg `-0.066` n `231`; crypto_major avg `-0.0822` n `8`; equity avg `0.0882` n `127`; fx avg `-0.0053` n `6`; index avg `0.0206` n `26`; metal avg `-0.0375` n `20`; unknown avg `-0.0107` n `791`
- 1h: commodity avg `-0.1906` n `12`; crypto_alt avg `0.3545` n `231`; crypto_major avg `-0.0607` n `8`; equity avg `0.3526` n `127`; fx avg `0.0061` n `6`; index avg `0.0646` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.1262` n `791`
- 4h: commodity avg `-0.2254` n `12`; crypto_alt avg `0.0797` n `231`; crypto_major avg `0.0023` n `8`; equity avg `-0.0028` n `127`; fx avg `-0.0069` n `6`; index avg `-0.0369` n `26`; metal avg `-0.2363` n `20`; unknown avg `0.021` n `775`
- 24h: commodity avg `0.1931` n `12`; crypto_alt avg `0.1984` n `231`; crypto_major avg `0.2837` n `8`; equity avg `1.4372` n `127`; fx avg `-0.0839` n `6`; index avg `0.2377` n `26`; metal avg `-0.3183` n `20`; unknown avg `0.3202` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal

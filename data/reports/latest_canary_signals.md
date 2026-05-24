# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T13:37:19.016925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1333` n `12`; crypto_alt avg `-0.246` n `228`; crypto_major avg `-0.1649` n `8`; equity avg `-0.051` n `67`; fx avg `0.0086` n `6`; index avg `-0.0195` n `23`; metal avg `-0.1157` n `18`; unknown avg `-0.0921` n `396`
- 1h: commodity avg `0.2089` n `12`; crypto_alt avg `-0.0382` n `228`; crypto_major avg `0.0977` n `8`; equity avg `-0.0191` n `67`; fx avg `0.0255` n `6`; index avg `-0.0633` n `23`; metal avg `-0.1852` n `18`; unknown avg `0.3289` n `396`
- 4h: commodity avg `0.3738` n `12`; crypto_alt avg `-0.8782` n `228`; crypto_major avg `-0.1625` n `8`; equity avg `0.2432` n `67`; fx avg `0.0139` n `6`; index avg `-0.1201` n `23`; metal avg `-0.2208` n `18`; unknown avg `0.7494` n `396`
- 24h: commodity avg `-2.4041` n `12`; crypto_alt avg `2.4735` n `228`; crypto_major avg `4.2083` n `8`; equity avg `2.5649` n `67`; fx avg `0.0863` n `6`; index avg `1.0302` n `23`; metal avg `1.0461` n `18`; unknown avg `1.8079` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
